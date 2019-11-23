FROM node:alpine

WORKDIR /usr/app

# to utilise the cached image
COPY ./package.json ./
RUN npm install
# to copy all that is required
COPY ./ ./

CMD ["npm", "start"]