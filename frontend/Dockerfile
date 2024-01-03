FROM node:latest

WORKDIR /app

COPY package*.json ./

RUN yarn install
RUN npm install @vue/cli-service --save-dev

COPY . .

EXPOSE 8080

CMD [ "yarn", "serve" ]