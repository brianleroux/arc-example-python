# Python demo

Install `package.json` deps and start the dev server:

```
npm i
npm start
```

## Deploy with CloudFormation

```
npm run package
```

This creates `sam.json` for deployment and prints out AWS CLI instructions.


## Deploy with Architect

Or let us handle that for you.

```
npm i -g @architect/architect
arc deploy  
```
