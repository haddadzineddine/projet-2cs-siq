const API_URL = import.meta.env.VITE_API_URL + "/run-deployment";

export const runDeployment = async (deployment) => {
    const res = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(deployment),
    });

    return await res.json();

}