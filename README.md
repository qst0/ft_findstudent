# Ceryneian Hind

Use the 42 API to find other students in the zones

Concepts
---

Before doing this in python, I thought it would be best to look at a curl
```
curl -X POST --data "grant_type=client_credentials&client_id=HERE_GOES_YOUR_UID&client_secret=HERE_GOES_YOUR_SECRET" https://api.intra.42.fr/oauth/token
```

Which will give you back a token!

Let's try something they show us on the 42 API documentation
```
curl -H "Authorization: Bearer HERE_GOES_YOUR_TOKEN" https://api.intra.42.fr/oauth/token/info
```

This will give you info back about the token

Just like this curl
```
curl https://api/intra.42.fr/oauth/token/info?&access_token=HERE_GOES_YOUR_TOKEN&token_type=bearer
```

So let's get some location data!
```
curl curl https://api/intra.42.fr/v2/users/myoung/locations?&access_token=HERE_GOES_YOUR_TOKEN&token_type=bearer
```

Setup
---

To use this python program you will need to run the following

```bash
pip install requests --user
pip install simplejson --user
```

[`requests`](http://docs.python-requests.org/en/latest/) is a library for easy http
[`simplejson`](https://simplejson.readthedocs.io/en/latest/) is a library I've used for pretty json output via `json.dumps`

Also set the enviorment variables for `FT42_UID` `FT42_SECRET` in `.zshrc`

```bash
FT42_UID=9b735bf8c218efdd93cd7224fefa6f0FAKE05af5cf93daefdd93c13636c37b23
FT42_SECRET=9b735bf8c3afbf8c21871381821670FAKE0256c37b245c5d1d8efdd93c3636c3
export FT42_UID
export FT42_SECRET
```
The `uid` and `secret` have to be your own, get them on [api.intra.42.fr](https://api.intra.42.fr/apidoc)

You will need to reload your .zshrc with `source .zshrc`

