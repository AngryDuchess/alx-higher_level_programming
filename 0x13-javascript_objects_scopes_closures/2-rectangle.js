#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w <= 0) || (h <=  0)){
    return this;
    }
    this.width = w;
    this.height = h;
  }

}
 /* if ((w <= 0) || (h <=  0)){
    this.r1 = new Rectangle();
  }*/

module.exports = Rectangle;
