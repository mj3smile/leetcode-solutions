/**
 * @param {Function} fn
 */
function memoize(fn) {
    const cache = new Map([
        [1, new Map()],
        [2, new Map()]
    ]);
    return function(...args) {
        key = args[0].toString() + (args.length > 1 ? ',' + args[1].toString() : '')
        if (cache.get(args.length).has(key)) {
            return cache.get(args.length).get(key)
        }
        
        result = fn(...args)
        cache.get(args.length).set(key, result)
        return result
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */