#!/usr/bin/env python
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # noqa

import kdewallet5

PERSONAL_FOLDERS = {
    'archive': '[Gmail]/All Mail',
    'drafts': '[Gmail]/Drafts',
    'flagged': '[Gmail]/Starred',
    'sent': '[Gmail]/Sent Mail',
    'trash': '[Gmail]/Trash',
}
REVERSE_PERSONAL_FOLDERS = {v: k for k, v in PERSONAL_FOLDERS.items()}
HIDE_FOLDERS = {'[Gmail]/Trash', '[Gmail]/Important', '[Gmail]/Spam'}


def get_password(wallet, folder_name, key):
    with kdewallet5.Wallet(wallet, "offlineimap") as wallet:
        return wallet.read_password(folder_name, key)


def personal_local_nametrans(folder_name):
    return PERSONAL_FOLDERS.get(folder_name, folder_name)


def personal_remote_nametrans(folder_name):
    return REVERSE_PERSONAL_FOLDERS.get(folder_name, folder_name)


def folder_filter(folder_name):
    return folder_name not in HIDE_FOLDERS


if __name__ == '__main__':
    print(get_password(sys.argv[1], sys.argv[2], sys.argv[3]))
