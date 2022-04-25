
@.uniqprintStringmain1 = private unnamed_addr constant [5 x i8] c"%d\n\00", align 1
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 1, i32* %x, align 4
	%uniqxmain2 = load i32, i32* %x, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain1, i64 0, i64 0) , i32 %uniqxmain2)
	ret i32 1
}