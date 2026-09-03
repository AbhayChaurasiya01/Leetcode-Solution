/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let map = new Map();

    // Add all objects from arr1
    for (let obj of arr1) {
        map.set(obj.id, obj);
    }

    // Add / merge objects from arr2
    for (let obj of arr2) {
        if (map.has(obj.id)) {
            map.set(obj.id, {
                ...map.get(obj.id),
                ...obj
            });
        } else {
            map.set(obj.id, obj);
        }
    }

    // Convert map to array and sort by id
    let result = Array.from(map.values());

    result.sort((a, b) => a.id - b.id);

    return result;
};