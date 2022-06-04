
@.uniqprintStringmain4 = private unnamed_addr constant [3 x i8] c"%s\00", align 1
@.uniqscanStringmain2 = private unnamed_addr constant [4 x i8] c"%5s\00", align 1
@.uniqprintStringmain1 = private unnamed_addr constant [28 x i8] c"Enter a 5-character string:\00", align 1
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%a = alloca [5 x i8], align 1
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([28 x i8], [28 x i8]* @.uniqprintStringmain1, i64 0, i64 0) )
	%temp0a= getelementptr inbounds [5 x i8], [5 x i8]* %a, i64 0, i32 None
%uniqamain3 = load i8, i8* %temp0a, align 1
	call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.uniqscanStringmain2, i64 0, i64 0), i8* %a)
	%temp1a= getelementptr inbounds [5 x i8], [5 x i8]* %a, i64 0, i32 None
%uniqamain5 = load i8, i8* %temp1a, align 1
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.uniqprintStringmain4, i64 0, i64 0) , i8 %uniqamain5)
	ret i32 1
}