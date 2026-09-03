/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const result = {};

    for (let item of this) {
        const key = fn(item);

        if (!result[key]) {
            result[key] = [];
        }

        result[key].push(item);
    }

    return result;
};

/**
 * Example:
 * [1, 2, 3].groupBy(String)
 * {"1":[1],"2":[2],"3":[3]}
 */