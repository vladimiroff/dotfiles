#!/usr/bin/env python
"""D-Bus client for KDE Wallet 5.

Example usage::

    >>> with kdewallet5.Wallet("my-super-secret-wallet", "foobar") as wallet:
    ...    my_password = wallet.read_password("secrets", "mothers_maiden_name")

"""
import dbus

BUS_NAME = 'org.kde.kwalletd5'
OBJECT_PATH = '/modules/kwalletd5'


class WalletClosedError(ValueError):
    pass


class CannotOpenWalletError(Exception):
    pass


class Wallet:
    """Simple D-Bus client for accessing KWallet."""
    _handle = dbus.Int32(-1)

    def __init__(self, name, app_name, wallet_id=0):
        """Open a session bus and get a proxy object to KWallet."""
        self.name = name
        self.app_name = app_name
        self.id = dbus.Int64(wallet_id)
        self._session_bus = dbus.SessionBus()
        self._connection = self._session_bus.get_object(BUS_NAME, OBJECT_PATH)

    def __enter__(self):
        if not self.open():
            raise CannotOpenWalletError

        return self

    def __exit__(self, type, value, traceback):
        self.close()
        return False

    def method(self, name):
        """Return a proxy representing the given D-Bus method."""
        return self._connection.get_dbus_method(name)

    def open(self):
        """Try to open a wallet and save given handle.

        It's NOT necessary to make sure the wallet is not already open. D-Bus
        will just return the same handle anyways.
        """
        self._handle = self.method('open')(self.name, self.id, self.app_name)
        return self._handle > 0

    @property
    def is_open(self):
        """Check that we have a handle for a wallet that is still open."""
        return self._handle > 0 and self.method('isOpen')(self.name)

    def close(self, force=False):
        """Close the wallet.

        This will delete the saved handle and will send a call to close the
        wallet. It's perfectly fine to close already closed wallet.

        By default D-Bus will actually close the wallet ONLY if there are no
        other applications using it. Set ``force`` to ``True`` to make sure the
        wallet will be closed even if it's being used by someone else.
        """
        self._handle = dbus.Int32(-1)
        return self.method('close')(self.name, dbus.Boolean(force))

    def read_password(self, folder, key):
        """Read password by given folder and key.

        If the wallet is not open this will raise ``WalletClosedError``.

        NOTE: If there isn't saved password with given key in given folder
        this will return an empty string instead of an error.
        """
        if not self.is_open:
            raise WalletClosedError("I/O operation on closed wallet.")

        return str(self.method('readPassword')(self._handle,
                                               folder, key, self.app_name))
