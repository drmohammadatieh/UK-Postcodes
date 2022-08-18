## UK Postcodes

This is an exercise on regular expressions as part of the Secure Software Development course of the CS PgCert at the University of Essex Online. 

## Instructions

The UK postcode system consists of a string that contains a number of characters and numbers – a typical example is ST7 9HV (this is not valid – see below for why). The rules for the pattern are available from idealpostcodes (2020).
Create a python program that implements a regex that complies with the rules provided above – test it against the examples provided.
Examples:
M1 1AA
M60 1NW
CR2 6XH
DN55 1PT
W1A 1HQ
EC1A 1BB

## The UK PostCode Format

Details about the Uk Postcode format can be found on this link https://ideal-postcodes.co.uk/guides/uk-postcode-format

## Quetions & Answers

### 1. How do you ensure your solution is not subject to an evil regex attack?

The regular expression pattern used was tested using the EGRET and ACRE tools found on this link
http://elarson.pythonanywhere.com.

Also, the regular expression pattern doesn't contain nested quantifiers and no backtracking is expected (Obielum, 2021).


### 2. What is ReDOS and what part do ‘Evil Regex’ play?

ReDOS is a regex denial of service attack. Basically, it exploits regex engines' vulnerabilities to overload a system rendering it unresponsive (Obielum, 2021)

### 3. What are the common problems associated with the use of regex? How can these be mitigated?

The problem with regex expressions is that they are susceptible to errors that can’t be detected easily. Some of the mitigations are by simplifying the regex expression as much as possible. Also, tools can be used to check the expressions for errors like EGRET and ACRE (Larson, 2016; Larson, 2018)

### 4. How and why could regex be used as part of a security solution?

Regex can be used as a part of a security solution by validating user input, creating firewall rules, and malware scanning (Li, 2020; Larson, 2016).

## References

Larson, E. (2016) Generating Evil Test Strings for Regular Expressions. Seattle University.

Larson, E. (2018) Automatic Checking of Regular Expressions. Seattle University.

Li, V. (2020) Regular Expressions: A Quick Intro for Security Professionals - DZone Security. 
Available from: https://dzone.com/articles/regular-expressions-a-quick-intro-for-security-pro [Accessed].

Obielum, G. (2021) How to protect against regex denial-of-service (ReDoS) attacks. Available from: https://blog.logrocket.com/protect-against-regex-denial-of-service-redos-attacks/ [Accessed].




