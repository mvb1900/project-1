const ARRROUTER = [
    // {
    //     path: `/`,
    //     name: "MyApp",
    //     meta: {
    //         title: "So sánh bản đồ",
    //     },
    //     component: () => import("../app_store_client/MyApp.vue"),
    // },
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
    item.path = "/" + path + item.path;
    return item;
});
}