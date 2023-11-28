FROM node:16-alpine as build_stage

ADD . /frontend
WORKDIR /frontend
RUN npm install
RUN npm run build

FROM node:16-alpine
WORKDIR /frontend
COPY --from=build_stage /frontend /frontend
CMD ["npm", "start"]