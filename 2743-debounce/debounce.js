/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timer;

    return function(...args) {
        // Cancel previous call
        clearTimeout(timer);

        // Schedule new call
        timer = setTimeout(() => {
            fn(...args);
        }, t);
    };
};