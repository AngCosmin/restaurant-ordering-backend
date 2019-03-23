FROM node:10-alpine

WORKDIR /node

ADD package.json /node/package.json
ADD package-lock.json /node/package-lock.json

RUN npm install

ADD . /node

CMD ["npm", "run", "serve"]
