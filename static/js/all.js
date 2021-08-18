(function () {

    var remarketingType = 'OTHER';

    // if current page is NOT cart page
    var cartPageActive = false; // unset cart page flag


    // if current page is NOT product page
    var productPageActive = false; // unset product page flag


    var collectionPageActive = false;


    var mainPageActive = true;

    if (remarketingType == 'OTHER') {
        var googleTagParams = {
            dynx_pagetype: 'home'
        };
    } else {
        var googleTagParams = {
            ecomm_pagetype: 'home'
        };
    }


    var cartPage = {
        active: cartPageActive, // flag true/false
        // if facebookEventParams is undefined set facebookEventParams = null
        facebookEventParams: typeof facebookEventParams !== 'undefined' ? facebookEventParams : null,
        googleTagParams: typeof googleTagParams !== 'undefined' ? googleTagParams : null
    };

    var productPage = {
        active: productPageActive, // flag true/false
        facebookEventParams: typeof facebookEventParams !== 'undefined' ? facebookEventParams : null,
        googleTagParams: typeof googleTagParams !== 'undefined' ? googleTagParams : null
    };

    var collectionPage = {
        active: collectionPageActive, // flag true/false
        facebookEventParams: null,
        googleTagParams: typeof googleTagParams !== 'undefined' ? googleTagParams : null
    };

    var mainPage = {
        active: mainPageActive,
        facebookEventParams: null,
        googleTagParams: typeof googleTagParams !== 'undefined' ? googleTagParams : null
    };

    // here we initialize our global object which contains all necessary information for
    // our all scripts which fired some google or facebook analytic events etc.
    // we should use some unique name to identify this object to avoid names conflict
    // relative to other global objects
    var hash = 'ROIHunterEasy_5a83c915b9f3150f071dd42973557062ac2f30b295a5b6393544410da07ecb27';
    window[hash] = {
        cartPage: cartPage,
        productPage: productPage,
        collectionPage: collectionPage,
        mainPage: mainPage,
        remarketingType: remarketingType
    };

    // begin: initialize our rheasy_fbq object for facebook tracking
    window[hash].rheasy_fbq = function () {
        if (arguments.length === 0) {
            return;
        }

        var pixelId, trackType, contentObj;     //get parameters:

        if (typeof arguments[0] === 'string') pixelId = arguments[0];       //param string PIXEL ID
        if (typeof arguments[1] === 'string') trackType = arguments[1];     //param string TRACK TYPE (PageView, Purchase)
        if (typeof arguments[2] === 'object') contentObj = arguments[2];    //param object (may be null):
                                                                            //    {value : subtotal_price,
                                                                            //     content_type : some_string,
                                                                            //     currency : shop_curency,
                                                                            //     contents : [{id, quantity, item_price}, ...] instance of array
                                                                            //    }

        var argumentsAreValid = typeof pixelId === 'string' && pixelId.replace(/\s+/gi, '') !== '' &&
            typeof trackType === 'string' && trackType.replace(/\s+/gi, '') !== '';

        if (!argumentsAreValid) {
            console.error('RH PIXEL - INVALID ARGUMENTS');
            return;
        }

        var params = [];
        params.push('id=' + encodeURIComponent(pixelId));
        switch (trackType) {
            case 'PageView':
            case 'ViewContent':
            case 'Search':
            case 'AddToCart':
            case 'InitiateCheckout':
            case 'AddPaymentInfo':
            case 'Lead':
            case 'CompleteRegistration':
            case 'Purchase':
            case 'AddToWishlist':
                params.push('ev=' + encodeURIComponent(trackType));
                break;
            default:
                console.error('RH PIXEL - BAD TRACKTYPE');
                return;
        }

        params.push('dl=' + encodeURIComponent(document.location.href));
        if (document.referrer) params.push('rl=' + encodeURIComponent(document.referrer));
        params.push('if=false');
        params.push('ts=' + new Date().getTime());

        /* Custom parameters to string */
        if (typeof contentObj === 'object') {                                               //`contents : [{id, quantity, item_price}, ...]` to string
            for (var u in contentObj) {
                if (typeof contentObj[u] === 'object' && contentObj[u] instanceof Array) {  // `[{id, quantity, item_price}, ...]` to string
                    if (contentObj[u].length > 0) {
                        for (var y = 0; y < contentObj[u].length; y++) {
                            if (typeof contentObj[u][y] === 'object') {                     // `{id, quantity, item_price}` to string
                                contentObj[u][y] = JSON.stringify(contentObj[u][y]);
                            }
                            contentObj[u][y] = (contentObj[u][y] + '')  //JSON to string
                                .replace(/^\s+|\s+$/gi, '')             //delete white characterts from begin on end of the string
                                .replace(/\s+/gi, ' ')                  //replace white characters inside string to ' '
                        }
                        params.push('cd[' + u + ']=' + encodeURIComponent(contentObj[u].join(',')   //create JSON array - [param1,param2,param3]
                            .replace(/^/gi, '[')
                            .replace(/$/gi, ']')))
                    }
                } else if (typeof contentObj[u] === 'string') {
                    params.push('cd[' + u + ']=' + encodeURIComponent(contentObj[u]));
                }
            }
        }

        var imgId = new Date().getTime();
        var img = document.createElement('img');
        img.id = 'fb_' + imgId, img.src = 'https://www.facebook.com/tr/?' + params.join('&'), img.width = 1, img.height = 1, img.style = 'display:none;';
        document.head.appendChild(img);
        window.setTimeout(function () {
            var t = document.getElementById('fb_' + imgId);
            t.parentElement.removeChild(t);
        }, 1000);

    };
    // end of: initializing rheasy_fbq object
})();