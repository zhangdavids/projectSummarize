function juggle() {
    var result = 0;
    for (var n=0; n<arguments.length; n++) {
        result += arguments[n];
    }
    this.result = result;
}

var ninja1 = {};
var ninja2 = {};

juggle.apply(ninja1, [1,2,3,4])
juggle.call(ninja2, 5,6,7,8)

console.log(ninja1.result)
console.log(ninja2.result)

// assert(ninja1.result === 10, "jungled via apply")
// assert(ninja2.result === 26, "jungled via call")        
