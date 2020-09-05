#ifndef TEST_H
#define TEST_H

#ifndef FOO_H
#define FOO_H

int func1(int);

#define FOO(x) x + 6

#endif // end if FOO_H

#ifndef BAR_H
#define BAR_H

int func1(int x)
{
    return x + 1;
}

#define BAR(x) x

#endif // end if BAR_H

#define TEST(x) x + 42

#endif // end if TEST_H
