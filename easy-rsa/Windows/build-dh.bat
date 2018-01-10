@echo off
cd %HOME%
rem build a dh file for the server side
openssl dhparam -out %KEY_DIR%/dh%DH_KEY_SIZE%.pem %DH_KEY_SIZE%
