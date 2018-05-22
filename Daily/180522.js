// function assert(bCondition, sErrorMsg) {
//     if (!bCondition) {
//         alert(sErrorMsg);
//         throw new Error(sErrorMsg);
//     }
    
// }

var outerValue = "samurai";
var later;

function outerFunction() {
    var innerValue = "ninja";
    
    function innerFunction() {
        assert(outerValue === "samurai", "I can see the samurai");
        assert(innerValue === "ninja", "I can see the ninja");
    }
    
    later = innerFunction;
    // console.log(outerValue);
    // console.log(innerValue);
}

outerFunction();

later();




// 在此是一个函数 有对应的工具库 用于测试模块 在自动化测试框架中用的最多 可以参考对应的nodejs 官方文档
// 理解闭包
