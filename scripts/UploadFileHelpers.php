<?php

namespace App\Http\Helpers;

use Illuminate\Support\Facades\Storage;

trait UploadFileHelpers
{
    /**
     * updload file
     *
     * @param  \Illuminate\Http\UploadedFile  $file
     * @param  string  $folder = 'uknown'
     * @return string|bool
     */
    public function upload_file(\Illuminate\Http\UploadedFile $file, string $folder = 'uknown')
    {
        return Storage::disk('public')->put($folder, $file);
    }

    /**
     * delete file
     *
     * @param string $file_path
     *
     * @return bool
     */
    public function delete_file(string $file_path)
    {
        return Storage::disk('public')->delete($file_path);
    }
}
