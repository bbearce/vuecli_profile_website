const history = require('connect-history-api-fallback');
const express = require('express');
const path = require('path');
const app = express();

// https://stackoverflow.com/questions/58845517/multi-page-vuejs-express-asset-issue-on-production
app.use(history({
    rewrites: [{
        from: /\/main_site/,
        to: '/main_site.html'
    }],
    
    htmlAcceptHeaders: ['text/html', 'application/xhtml+xml']
    
}));
app.use(express.static(path.join(__dirname, 'dist')))

const port = process.env.PORT || 3000;
app.listen(port);
