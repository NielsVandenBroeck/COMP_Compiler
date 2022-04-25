
@.procentD = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	ret i32 0
}