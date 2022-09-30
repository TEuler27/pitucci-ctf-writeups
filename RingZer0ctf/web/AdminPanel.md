# Admin Panel

### Author

[Mr.Un1k0d3r](https://twitter.com/mrun1k0d3r)

### Description

No description

## Solution
 
We need to somehow gain access to the admin panel. Analyzing the request with burpsuite we realized that it was actually two responses: the first replied with code 302 and redirected us to the error page. Inspecting the response we can see the full admin panel code that contains a button:

```
<form action="/challenges/104/" method="get">
	<input type="hidden" class="form-control" value="yesIwantaflag" name="showflagforme" />
	<input type="submit" class="btn btn-success form-control" value="Generate" style="margin-top: 12px" />
</form>
```

Just browsing the page `/challenges/104/?showflagforme=yesIwantaflag` gives us the flag.
