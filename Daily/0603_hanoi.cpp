//
//  main.cpp
//  Hanoi
//
//  Created by 张俊 on 2018/6/3.
//  Copyright © 2018年 张俊. All rights reserved.
//

#include <iostream>
int s=0;

void move(char x, char y){
    std::cout<<x<<"--->"<<y<<std::endl;
    s++;
}

void hanoi(int n, char a, char b, char c){
    if(n==1)
        move(a, c);
    else
    {
        hanoi(n-1, a, c, b);
        move(a, c);
        hanoi(n-1, b, a, c);
    }
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int m;
    std::cout<<"请输入盘子数： ";
    std::cin>>m;
    std::cout<<"移动"<<m<<"个盘子的过程如下： "<<std::endl;
    hanoi(m, 'A', 'B', 'C');
    std::cout << "一共移动"<<s<<"次"<<std::endl;
    return 0;
}
