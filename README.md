# browser-power
File utilities for our browsers - the future of command line utilities

# What is this
This is an experiment to see how capable our modern browsers are. I want to create a set of file tools that run completely on the client side with no data being transferred to a server. This way we can have a new generation of browser based file tools that can start replacing their command-line versions.

# What's next
I'd like to see all basic operations on local files be implemented in the browser. How about different compression tools, diff, file editor, hex editor, hashing and encryption tools, search and replace tools, etc. How about using these tools to process files and then pipe the result directly to our cloud storage providers or third-party APIs?

# File Tools in Your Browser
In order to build these tools I had to leverage some awesome open source javascript libraries:
* [StreamSaver.js](https://github.com/jimmywarting/StreamSaver.js) - for downloading a file efficiently
* [web-streams-polyfill](https://github.com/MattiasBuelens/web-streams-polyfill) - for providing access to streaming functionality on different browsers
* [forge](https://github.com/digitalbazaar/forge) - for encrypting and hashing files efficiently
* [pako](https://github.com/nodeca/pako) - for fast compression with zlib

## File Encryption and Decryption
File encryption uses AES-GCM mode of encryption. The password specified by the user is processed by PBKDF2 using 100K iteration rounds. This takes a couple of seconds. I generate 128 bit salt that is also supplied to the PBKDF2 function. I'm curious to see if a better memory hard password strengthening function can be applied using javascript such as scrypt or argon2.

The file encryption and decryption run at 9 MB/s on my macbook pro. This is not too bad but it can't compare to actual local disk utilities. The memory footprint is constant where the file is read in 512Kb chunks. This seems to work well.

The encrypted file structure is as follows:
```
| 128-bit salt | encrypted file contents | 128-bit tag |
```

## File Hasher
The file hasher only supports SHA-256. It is much slower then the command line tool `sha256sum`. For the same file the browser version takes 13 seconds to hash 
100MB file but the command line tool takes 2 seconds. If you're looking to hash smaller files it is perfectly ok to do this in the browser. The hashing takes constant memory and the file is read in 1 MB chunks.

## File Compressor
The file compressor uses zlib with level 9 to compress files in the browser. The files are read and compressed/decompressed in chunks. The compressor works on 1Mb chunks while the decompressor works on 1Kb chunks. If you have really well compressed data such as 10GBs of zeros you might run out of memory reall quick if you read 1Mb of compressed data and try to decompress it in memory. The progress is displayed every 1Mb of read compressed data in order to avoid overworking the browser.

Keep in mind that the download progress will not be accurate for both compression and decompression because we don't know the compressed or decompressed size in advanced. The progress displayed on the page will be accurate as it represents how much from the source file we've processed.

## Run the File Tools
Encrypt a file: https://stanimirivanovde.github.io/browser-power/encrypt-file.html

Decrypt a file: https://stanimirivanovde.github.io/browser-power/decrypt-file.html

Hash a file: https://stanimirivanovde.github.io/browser-power/hash-file.html

Compress a file: https://stanimirivanovde.github.io/browser-power/compress-file.html

Decompress a file: https://stanimirivanovde.github.io/browser-power/decompress-file.html
