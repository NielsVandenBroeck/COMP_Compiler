
@.uniqprintStringmain4 = private unnamed_addr constant [7 x i8] c"%d%f%c\00", align 1
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%uniqprintTempmain1 = alloca i32, align 4
	store i32 10, i32* %uniqprintTempmain1, align 4
	%uniqprintTempmain2 = alloca float, align 4
	store float 0x3fe0000000000000, float* %uniqprintTempmain2, align 4
	%uniqprintTempmain3 = alloca i8, align 1
	store i8 37, i8* %uniqprintTempmain3, align 1
	%uniquniqprintTempmain1main5 = load i32, i32* %uniqprintTempmain1, align 4
	%uniquniqprintTempmain2main6 = load float, float* %uniqprintTempmain2, align 4
	%uniqmain7 = fpext float %uniquniqprintTempmain2main6 to double
	%uniquniqprintTempmain3main8 = load i8, i8* %uniqprintTempmain3, align 1
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.uniqprintStringmain4, i64 0, i64 0) , i32 %uniquniqprintTempmain1main5, double %uniqmain7, i8 %uniquniqprintTempmain3main8)
	ret i32 0
}