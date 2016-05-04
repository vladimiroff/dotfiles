#!/bin/sh

crypto_pass=$(kwallet-query -l kdewallet -f Passwords -r pCloud | jq .crypto -r)
pcloudcc -u kiril@vladimiroff.org -d -c $crypto_pass
