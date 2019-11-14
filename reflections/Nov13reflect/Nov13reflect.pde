float dia(x, y) {
  for (int i = 0; i < x; i++) {
    for (int n = 0; n < y; n++) {
    rect(0,i,n,0)
    }
  }
}
//originally I had messed around with values of rect in setup
//then I decided to try to make nesting loops to make something 'pixel by pixel' as we've done before
//not quite working...
void setup() {
  size(800,600);
  background(255);
  dia(800,600);
}
