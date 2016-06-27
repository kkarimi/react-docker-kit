const generalConfig = {
  version: '0.1',
  googleApiKey: 'xxxxx',
  tokenCookieName: 'token',
  localStorageUserKey: 'user'
};

const dev = {
  serverUrl: 'http://127.0.0.1',
  port: '5000'
};

const production = {
  serverUrl: 'http://192.168.99.100',
  port: '80'
};


const env = process.env.NODE_ENV;
const envConfig = eval(`${env}`);

module.exports = Object.assign({}, generalConfig, envConfig);
