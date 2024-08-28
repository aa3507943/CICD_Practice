import http from "k6/http";
import { check, sleep } from "k6";

var url = "http://test.k6.io"

export default function () {
    const res = http.get(url);
    check(res, { "status was 200": (r) => r.status == 200 });
    sleep(1);
};

export const options = {
    stages: [
        {  duration: "10s", target: 1000 },
        {  duration: "2m", target: 1000 },
        {  duration: "10s", target: 0 },
    ]
};