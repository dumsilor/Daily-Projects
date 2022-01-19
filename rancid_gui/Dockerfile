# Specify a base imagge
#FROM alpine
#base image alpine nile node alada kore install korte hobe so node er alphine version use korb
FROM node:alpine


#Basic Copy root directory te copy kore, eta er jonno
#base working directory below command diye set kore dea jay
#eta te /usr/app er vitore shob copy hobe
WORKDIR /usr/app

#Copy local files(dependencies) to container ##   COPY local container
#because npm run install er jonno only packege.json file lage
#Also onno kono file e change korle whole step abar repeat hobe
COPY ./package.json ./

# Install some dependencies
RUN npm install

COPY ./ ./

#Default Command
CMD ["npm","start"]