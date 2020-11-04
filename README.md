# browser-power
A showcase of client side javascript that can run in the browser

# What is this
This is an experiment to see how capable our modern browsers are. I want to create a set of file tools that run completely on the client side with no data being transferred to a server. This way we can have a new generation of browser based file tools that can start replacing their command-line versions.

# What's next
I'd like to see all basic operations on local files be implemented in the browser. How about different compression tools, diff, file editor, hex editor, hashing and encryption tools, search and replace tools, etc. How about using these tools to process files and then pipe the result directly to our cloud storage providers or third-party APIs?

# File Tools in Your Browser
## File Encryption and Decryption
File encryption uses AES-GCM mode of encryption. The password specified by the user is processed by PBKDF2 using 100K iteration rounds. This takes a couple of seconds. I generate 128 bit salt that is also supplied to the PBKDF2 function. I'm curious to see if a better memory hard password strengthening function can be applied using javascript such as scrypt or argon2.

The file encryption and decryption run at 9 MB/s on my macbook pro. This is not too bad but it can't compare to actual local disk utilities. The memory footprint is constant where the file is read in 512Kb chunks. This seems to work well.

The encrypted file structure is as follows:
```
| 128-bit salt | encrypted file contents | 128-bit tag |
```

Encrypt a file: https://stanimirivanovde.github.io/browser-power/encrypt-file.html
Decrypt a file: https://stanimirivanovde.github.io/browser-power/decrypt-file.html

## File Hasher
The file hasher only supports SHA-256. It is much slower then the command line tool `sha256sum`. For the same file the browser version takes 13 seconds to hash 
100MB file but the command line tool takes 2 seconds. If you're looking to hash smaller files it is perfectly ok to do this in the browser. The hashing takes constant memory and the file is read in 1 MB chunks.

Hash a file: Decrypt a file: https://stanimirivanovde.github.io/browser-power/hash-file.html
