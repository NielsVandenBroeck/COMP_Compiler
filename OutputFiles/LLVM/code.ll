
@.uniqprintStringmain5 = private unnamed_addr constant [11 x i8] c"%d; %d; %d\00", align 1
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 10, i32* %x, align 4
	%xp = alloca i32*, align 8
	store i32* %x, i32** %xp, align 8
	%xpp = alloca i32*, align 8
	store i32* %xp, i32** %xpp, align 8
	%uniqxppointerToValuemain10 = load i32*, i32** %xp, align 8
	%uniqxppointerToValuemain1 = load i32, i32* %uniqxppointerToValuemain10, align 8
	%uniqxppointerToValuemain2 = alloca i32, align 4
	store i32 %uniqxppointerToValuemain1, i32* %uniqxppointerToValuemain2, align 4
	%uniqxpppointerToValuemain30 = load i32*, i32** %xpp, align 8
	%uniqxpppointerToValuemain3 = load i32, i32* %uniqxpppointerToValuemain30, align 8
	%uniqxpppointerToValuemain4 = alloca i32, align 4
	store i32 %uniqxpppointerToValuemain3, i32* %uniqxpppointerToValuemain4, align 4
	%uniqxmain6 = load i32, i32* %x, align 4
	%uniquniqxppointerToValuemain2main7 = load i32, i32* %uniqxppointerToValuemain2, align 4
	%uniquniqxpppointerToValuemain4main8 = load i32, i32* %uniqxpppointerToValuemain4, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([11 x i8], [11 x i8]* @.uniqprintStringmain5, i64 0, i64 0) , i32 %uniqxmain6, i32 %uniquniqxppointerToValuemain2main7, i32 %uniquniqxpppointerToValuemain4main8)
	ret i32 1
}