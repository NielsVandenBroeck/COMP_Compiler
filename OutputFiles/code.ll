
@.procentD = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	%y = alloca i32, align 4
	store i32 x, i32* %y, align 4
	%uniqymain1 = load i32, i32* %y, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.procentD, i64 0, i64 0), i32 %uniqymain1)
	ret i32 0
}