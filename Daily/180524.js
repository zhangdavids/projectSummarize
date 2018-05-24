
function Ninja() {
    var feints = 0;
    this.getFeints = () => feints
    this.feint = function() {
        feints++;
    };
}

var ninja1 = new Ninja();
ninja1.feint();

console.log(ninja1.feints)
console.log(ninja1.getFeints())

var ninja2 = new Ninja()
console.log(ninja2.getFeints())
