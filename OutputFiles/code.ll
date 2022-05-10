
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%i = alloca i32, align 4
	store i32 -4, i32* %i, align 4
	%uniqmain1 = alloca i32, align 4
	store i32 1, i32* %uniqmain1, align 4
	%uniqimain2 = load i32, i32* %i, align 4
	%uniquniqmain1main3 = load i32, i32* %uniqmain1, align 4
	%uniqmain4 = add i32 %uniqimain2, %uniquniqmain1main3
	store i32 %uniqmain4, i32* %i, align 4
	ret i32 1
}