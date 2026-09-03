/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    // If it is not an object or is null
    if (obj === null || typeof obj !== "object") {
        return obj;
    }

    // If it is an array
    if (Array.isArray(obj)) {
        return obj
            .filter(Boolean)
            .map(compactObject);
    }

    // If it is an object
    let result = {};

    for (let key in obj) {
        let value = compactObject(obj[key]);

        if (value) {
            result[key] = value;
        }
    }

    return result;
};