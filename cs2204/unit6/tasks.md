## Memo

- Data Compression Techniques
  - Data Compression ratios
    - Equals compression power
  - Lossless vs Lossy Compression
    - Lossless: No data loss, e.g., ZIP, PNG
    - Lossy: Some data loss, e.g., JPEG, MP3
    - Methods wchich should be used depend on the use case
    - Lossy is used for images, audio, video
  - Lossy data compression techniques
    - Transform coding
      - Converts data to a different format
      - Example: JPEG uses DCT (Discrete Cosine Transform)
    - Quantization
      - Reduces precision of data
      - Example: Reducing color depth in images
    - Entropy coding
      - Encodes data based on frequency of occurrence
      - Example: Huffman coding, Arithmetic coding
    - The advantage of lossy compression over lossless compression is that it can achieve higher compression ratios, resulting in smaller file sizes. This is particularly beneficial for multimedia files such as images, audio, and video, where some loss of quality may be acceptable in exchange for reduced storage space and faster transmission times. Lossy compression techniques can significantly reduce the amount of data that needs to be stored or transmitted, making them ideal for applications where bandwidth and storage are limited.
    - Two basic schemes of lossy compression are transform coding and predictive coding. 
      - transform coding converts the data into a different format, such as the Discrete Cosine Transform (DCT) used in JPEG compression. This transformation allows for the separation of important information from less important information, enabling more efficient compression.
      - predictive coding, on the other hand, predicts the value of a data point based on previous data points and encodes only the difference between the predicted and actual values. This method is commonly used in audio and video compression, where temporal redundancy can be exploited to achieve higher compression ratios.
  - Lossless data compression techniques
    - Run-length encoding (RLE)
      - Replaces consecutive identical elements with a single element and a count
      - Example: "AAAAA" becomes "A5", 1111111000000011111000000111111 becomes 1(6)0(7)1(5)
    - Huffman coding
      - Uses variable-length codes for different symbols based on their frequency
      - Sending data is two types
        - Static Huffman coding: Uses a fixed codebook for the entire data set
        - Adaptive Huffman coding: Builds the codebook dynamically as data is processed
      - Steps to create a Huffman tree
        1. Count the frequency of each symbol in the data set.
        2. Create a leaf node for each symbol and build a priority queue (min-heap) based on their frequencies.
        3. While there is more than one node in the queue:
           - Remove the two nodes with the lowest frequency.
           - Create a new internal node with these two nodes as children and a frequency equal to the sum of their frequencies.
           - Insert the new node back into the priority queue.
        4. The remaining node is the root of the Huffman tree.
      - Example: More frequent symbols get shorter codes
    - Lempel-Ziv-Welch (LZW)
      - Builds a dictionary of substrings and replaces them with shorter codes
      - Advantage: No need to transmit the dictionary
      - How does LZW work?
        1. Initialize the dictionary with all possible single-character strings.
        2. Start with an empty string (current_string).
        3. Read the next character (next_char) from the input data.
        4. If current_string + next_char exists in the dictionary:
           - Set current_string to current_string + next_char.
        5. Else:
           - Output the code for current_string.
           - Add current_string + next_char to the dictionary.
           - Set current_string to next_char.
        6. Repeat steps 3-5 until all input data is processed.
        7. Output the code for current_string if it is not empty.
      - Example: Used in GIF and TIFF formats
    - The advantage of lossless compression over lossy compression is that it preserves the original data without any loss of information. This is crucial for applications where data integrity is essential, such as text documents, executable files, and certain types of images (e.g., medical imaging). Lossless compression techniques ensure that the decompressed data is identical to the original data, making them suitable for scenarios where accuracy and fidelity are paramount. Additionally, lossless compression can be used in conjunction with lossy compression to provide a balance between quality and file size, allowing users to choose the appropriate level of compression based on their specific needs.

## Discussion Forum:
Scenario: 

You've been assigned the challenge of creating a comprehensive communication framework for a multi-tiered web application, which also includes the development of a secure communication protocol for a decentralized peer-to-peer messaging application. This entails designing a communication system that not only facilitates interactions between the presentation, application, and data layers of the web app but also ensures secure and efficient messaging among decentralized peers. 

Based on the given scenario, answer the following questions: 


1. Compose a strategy to integrate session layer protocols such as TLS/SSL to ensure secure and reliable communication between these layers. Consider factors like session establishment, maintenance, and termination, as well as potential challenges like scalability and compatibility with different client-server architectures.
2. Regarding the need of decentralized peer-to-peer messaging application:
    a. How would you integrate advanced data compression techniques at the presentation layer to optimize bandwidth utilization and enhance the efficiency of message transmission?
    b. Additionally, propose methods to incorporate encryption algorithms into the protocol to ensure end-to-end security and confidentiality of messages exchanged between users.

Answer:
1. To integrate session layer protocols such as TLS/SSL for secure and reliable communication between the presentation, application, and data layers of a multi-tiered web application, I would implement the following strategy:
- **Session Establishment**: I would ensure that the TLS/SSL handshake process is initiated when a client connects to the server. This involves the exchange of cryptographic keys and the establishment of a secure session. I would use strong cipher suites and enforce the use of the latest TLS version to enhance security. Additionally, I would implement certificate validation to prevent man-in-the-middle attacks.
- **Session Maintenance**: To maintain the session, I would implement session resumption techniques such as session IDs or session tickets. This would allow clients to reconnect without going through the full handshake process, reducing latency and improving performance. I would also monitor session activity and implement timeouts to terminate inactive sessions, ensuring that resources are not wasted on idle connections.
- **Session Termination**: I would ensure that sessions are properly terminated when a user logs out or when the session expires. This would involve securely closing the connection and invalidating any session tokens to prevent unauthorized access.
- **Scalability**: To address scalability challenges, I would implement load balancing techniques to distribute incoming traffic across multiple servers. This would help manage high volumes of connections and ensure that the application remains responsive. I would also consider using a content delivery network (CDN) to cache static content and reduce the load on the origin server.
- **Compatibility**: To ensure compatibility with different client-server architectures, I would implement fallback mechanisms that allow clients to connect using older versions of TLS/SSL if necessary. However, I would enforce strict security policies to discourage the use of outdated protocols and encourage clients to upgrade to more secure versions.
2. Regarding the need of decentralized peer-to-peer messaging application:
   a. To integrate advanced data compression techniques at the presentation layer of a decentralized peer-to-peer messaging application, I would implement the following methods:
- **Lossless Compression**: I would use lossless compression algorithms such as Huffman coding or Lempel-Ziv-Welch (LZW) to compress text messages. This would ensure that the original message can be perfectly reconstructed upon decompression, which is crucial for maintaining the integrity of the communication.
- **Lossy Compression**: For multimedia messages (e.g., images, audio, video), I would implement lossy compression techniques such as JPEG for images and MP3 for audio. This would significantly reduce the size of multimedia files, optimizing bandwidth utilization while maintaining acceptable quality.
- **Adaptive Compression**: I would implement adaptive compression techniques that adjust the compression level based on the network conditions. For example, if the network is congested, the application could increase the compression level to reduce data size, while in optimal conditions, it could use lower compression to preserve quality.
   b. To incorporate encryption algorithms into the protocol to ensure end-to-end security and confidentiality of messages exchanged between users in a decentralized peer-to-peer messaging application, I would propose the following methods:
- **Asymmetric Encryption**: I would use asymmetric encryption algorithms such as RSA or ECC (Elliptic Curve Cryptography) for key exchange. Each user would have a public-private key pair, allowing them to securely exchange symmetric keys for encrypting messages.
- **Symmetric Encryption**: For the actual message encryption, I would use symmetric encryption algorithms such as AES (Advanced Encryption Standard). This would provide fast and efficient encryption and decryption of messages while ensuring confidentiality.
- **Digital Signatures**: To ensure message authenticity and integrity, I would implement digital signatures using algorithms like RSA or ECDSA (Elliptic Curve Digital Signature Algorithm). This would allow users to verify that messages have not been tampered with and confirm the identity of the sender.
- **Perfect Forward Secrecy**: I would implement perfect forward secrecy (PFS) to ensure that even if a user's private key is compromised, past communications remain secure. This would involve generating new session keys for each communication session, preventing the decryption of previous messages.
- **End-to-End Encryption**: I would ensure that messages are encrypted on the sender's device and only decrypted on the recipient's device. This would prevent intermediaries, including servers, from accessing the content of the messages, ensuring true end-to-end security.
Overall, this strategy would provide a robust framework for secure and efficient communication in both the multi-tiered web application and the decentralized peer-to-peer messaging application, addressing key challenges related to security, scalability, and performance.