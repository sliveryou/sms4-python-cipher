var count = 0;
console.log(count)

function plus1(x) {
    return x + 1;
}
count = plus1(count);
console.log(count)
console.log(count)

var a = [];
a.push(1, 2, 3);
console.log(a);
a.reverse()
console.log(a)

function abs(x) {
    if (x >= 0) {
        return x;
    }
    else {
        return -x;
    }
}

console.log(abs(-7))

var s = 'hello'
for (var i = 0; i <= 3; i++) {
    console.log(s[i])
}

var i = 11;
console.log(i.toString(10))
console.log(i.toString(8))
console.log(i.toString(16))
console.log(Number.MAX_VALUE)

var s = '001234.78.9'
console.log(parseFloat(s))
console.log(parseInt(s))
console.log(Number(s))
console.log(Number(''))
console.log(parseInt(''))

console.log(null == 0)
console.log(!!'0')
console.log()

console.log(typeof 95)
console.log(typeof 'hello')
console.log(typeof [1, 2, 3])
console.log(typeof null)
console.log(typeof undefined)
console.log(typeof function foo() { return 0 })
console.log(typeof true)
console.log(typeof typeof null)

var age
console.log(typeof age)
console.log(typeof name)

function test() {
    var foo = 0;
}
console.log(test())

console.log(null == undefined)
console.log(null === undefined)

console.log(0o27)
console.log(0xaf)

console.log(0.1 + 0.2 == 0.3)

console.log(Number.MAX_VALUE, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY)
console.log(isFinite(5678))
console.log(isFinite(Infinity))
console.log(6789 / 0)
console.log()

console.log(isNaN(10))
console.log(isNaN('10'))
console.log(isNaN('test'))
console.log(isNaN(true))
console.log(isNaN(NaN))
console.log()

obj1 = {valueOf: function () {
    return 3;
}}

obj2 = {valueOf: function() {
    return 'hello';
}, toString: function() {
    return '3'
}}

console.log(isNaN(obj1))
console.log(isNaN(obj2))

console.log(Number(obj1))
console.log(Number(obj2))
