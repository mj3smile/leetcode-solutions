/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    args = []
    return function curried(...a) {
        for (var i = 0; i < a.length; i++) {
            args.push(a[i])
        }
        if (args.length == fn.length) {
            return fn(...args)
        }
        return function(...a) {
            return curried(...a)
        }
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
