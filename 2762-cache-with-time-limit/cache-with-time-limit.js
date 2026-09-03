/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration
 * @return {boolean}
 */
var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration
 * @return {boolean}
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let exists = this.cache.has(key);

    // If key already exists, cancel old timer
    if (exists) {
        clearTimeout(this.cache.get(key).timer);
    }

    // Create new timer
    let timer = setTimeout(() => {
        this.cache.delete(key);
    }, duration);

    // Store value and timer
    this.cache.set(key, {
        value: value,
        timer: timer
    });

    return exists;
};

/**
 * @param {number} key
 * @return {number}
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.cache.has(key)) {
        return this.cache.get(key).value;
    }

    return -1;
};

/**
 * @return {number}
 */
TimeLimitedCache.prototype.count = function() {
    return this.cache.size;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache();
 * obj.set(1, 42, 1000); // false
 * obj.get(1); // 42
 * obj.count(); // 1
 */