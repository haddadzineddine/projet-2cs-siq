const API_URL = import.meta.env.VITE_API_URL + "/login";

import { removeItem } from "./LocalStorageService";

export const login = (credientials, callback) => {
    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(credientials),
    })
        .then((res) => res.json())
        .then((res) => {
            callback(res);
        });
}

export const logout = () => {
    removeItem("_token");
}
