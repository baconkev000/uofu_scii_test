FROM node:latest

WORKDIR /app

COPY package*.json ./

RUN apk add yarn

RUN yarn global add @vue/cli @vue/cli-service

RUN yarn install

COPY . .

EXPOSE 8080

CMD [ "yarn", "serve" ]