(function (window) {
    "use strict";

    var setts = {
        "SERVER_URL": "{{api_server_domain}}",
        "HOME_PAGE_NAME": "scheduling",
        "DEBUG": false,
        "ACTIONS": {
            "RESTRICT": []
        },
        "CREDZ": {
            "client_id": "emrapp224",
            "client_secret": "emrapp@siri"
        },
        "AUTH": {
            "SERVER_DOMAIN": "{{api_server_domain}}",
            "TOKEN_URL": "/o/token/",
            "REVOKE_TOKEN_URL": "/o/revoke_token/",
            "USER_INFO_URL": "/me/",
            "REDIRECT_URL": "/complete/",
            "USER_PROFILE": "/manage/profile/"
        }
    };
    setts.CREDZ.token_url = setts.SERVER_URL + setts.AUTH.TOKEN_URL;
    setts.CREDZ.revoke_url = setts.SERVER_URL + setts.AUTH.REVOKE_TOKEN_URL;

    window.EMR_SETTINGS = setts;

})(window);
