// Setup
var VK = require('vksdk');
var vk = new VK({
   'appId'     : 5098770,
   'appSecret' : 'Mao7JPCkkqVGd4gIjcOQ',
   'language'  : 'ru'
});


/**
 * Request server methods
 */

// Setup server access token for server API methods
vk.on('serverTokenReady', function(_o) {
    // Here will be server access token
    vk.setToken(_o.access_token);
});

// Turn on requests with access tokens
vk.setSecureRequests(true);

// Request server API method
vk.request('secure.getSMSHistory', {}, function(_dd) {
    console.log(_dd);
});

/**
 * Request client methods
 */
// First you have to pass access_token from client side SJ code
vk.setToken(access_token);

// Request 'users.get' method
vk.request('users.get', {'user_id' : 1}, function(_o) {
    console.log(_o);
});
