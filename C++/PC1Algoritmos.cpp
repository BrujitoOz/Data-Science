#include <iostream>
#include <functional>
#include <vector>
using namespace std;

typedef function<float(vector<float>)> lambda;
float pregunta1(lambda lmb)
{
  vector<float> nums(1<<15, 0.0);
  for (int i = 0; i < nums.size(); ++i)
  {
    if(i%1<<1 == 0) nums[i] = i * 3.7;
    if(i%1<<3 == 0) nums[i] = i * 1.7;
    if(i%1<<5 == 0) nums[i] = i * 7.7;
    if(i%3<<2 == 0) nums[i] = i * 5.7;
    if(i%3<<4 == 0) nums[i] = i * 9.7;
    nums[i] += i / (1 + nums[i]);
  }
  
  return lmb(nums);
}
float pregunta2(lambda lmb)
{
  vector<float> nums((1<<16)+1, 0.0);
  nums[0] = 2.71828;
  for (int i = 1; i < nums.size(); ++i)
  {
    if(i%3==0) nums[i] += i / ((1<<1)+nums[i-1]);
    if(i%5==0) nums[i] += i / ((1<<2)+nums[i-1]);
    if(i%7==0) nums[i] += i / ((1<<3)+nums[i-1]);
  }
  return lmb(nums);
}
int main()
{
    auto lambda = [](vector<float> vec)
    {
        float s = 0;
        for (int i = 0; i < vec.size(); i++)
        {
            s += vec[i];
        }
        return s;
    };
    cout << pregunta1(lambda);
    cout << pregunta2(lambda);

    return 0;
}