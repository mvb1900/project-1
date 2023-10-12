const APP_NAME = "Todo_List"

const ARRROUTER = [
    {
        path: `/`,
        name: "Home",
        meta: {
            title: "Trang chủ",
        },
        component: () => import("./views/index.vue"),
    },
    // {
    //     path: `/:appId`,
    //     name: "MyAppDetail",
    //     meta: {
    //         title: "Chi tiết ứng dụng của tôi",
    //     },
    //     component: () => import("../app_store_client/MyAppDetail.vue"),
    // }
]

export default function (path) {
return ARRROUTER.map((item) => {
    item.name = APP_NAME + "_" + item.name
    item.path = "/" + path + item.path;
    return item;
});
}