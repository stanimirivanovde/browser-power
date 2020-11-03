# browser-power
A showcase of client side javascript that can run in the browser

# What is this
This is an experiment to see how capable our modern browsers are. As a start I'm using state of the art AES-GCM encryption to encrypt and decrypt files of arbitrary sizes. It runs in constant memory using chunking and shows how capable modern browsers are. You can run this file encryption/decryption on any operating system, any device and it should work out of the box. The operations are done completely client side so no data leaves your computer. It showcases how your browser can now be used to re-implement most command line utilities in a cross-platform way without the need to download extra tools and applications.

# What's next
I'd like to see all basic operations on local files be implemented in the browser. This includes compression and basic editing etc.

# File Encryption and Decryption
File encryption uses AES-GCM mode of encryption. The password specified by the user is processed by PBKDF2 using 100K iteration rounds. This takes a couple of seconds. I generate 128 bit salt that is also supplied to the PBKDF2 function. I'm curious to see if a better memory hard password strengthening function can be applied using javascript such as scrypt or argon2.

The file encryption and decryption run at 9 MB/s on my macbook pro. This is not too bad but it can't compare to actual local disk utilities. The memory footprint is constant where the file is read in 1 MB chunks. This seems to work well.

The encrypted file structure is as follows:
```
| 128-bit salt | file contents | 128-bit tag |
```

# File Hasher
The file hasher only supports SHA-256. It is much slower then the command line tool `sha256sum`. For the same file the browser version takes 13 seconds to hash 100MB file but the command line tool takes 2 seconds. If you're looking to hash smaller files it is perfectly ok to do this in the browser. The hashing takes constant memory and the file is read in 1 MB chunks.
