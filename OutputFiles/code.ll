
@.uniqprintStringmain11 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain8 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain5 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain2 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%uniqprintTempmain1 = alloca i32, align 4
	store i32 2, i32* %uniqprintTempmain1, align 4
	%uniquniqprintTempmain1main3 = load i32, i32* %uniqprintTempmain1, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain2, i64 0, i64 0) , i32 %uniquniqprintTempmain1main3)
	%uniqprintTempmain4 = alloca i32, align 4
	store i32 2, i32* %uniqprintTempmain4, align 4
	%uniquniqprintTempmain4main6 = load i32, i32* %uniqprintTempmain4, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain5, i64 0, i64 0) , i32 %uniquniqprintTempmain4main6)
	%uniqprintTempmain7 = alloca i32, align 4
	store i32 10, i32* %uniqprintTempmain7, align 4
	%uniquniqprintTempmain7main9 = load i32, i32* %uniqprintTempmain7, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain8, i64 0, i64 0) , i32 %uniquniqprintTempmain7main9)
	%uniqprintTempmain10 = alloca i32, align 4
	store i32 10, i32* %uniqprintTempmain10, align 4
	%uniquniqprintTempmain10main12 = load i32, i32* %uniqprintTempmain10, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain11, i64 0, i64 0) , i32 %uniquniqprintTempmain10main12)
	ret i32 1
}